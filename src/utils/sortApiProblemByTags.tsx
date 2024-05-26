import ProblemTag from "../assets/database/problemTag.json";
import { ProbFromApi, CategorizedProblem } from "../interfaces";

export const preprocessProblemList = (
  data: ProbFromApi,
  algorithmFilter: string[]
): CategorizedProblem[] => {
  const categorizedProblems: CategorizedProblem[] = ProblemTag.map((tag) => ({
    kr: tag.kr,
    en: tag.en,
    bojTagId: tag.bojTagId,
    bgColor: tag.bgColor,
    problemList: [],
  }));

  const uncategorizedProblems: CategorizedProblem = {
    kr: "기타",
    en: "miscellaneous",
    bojTagId: -1,
    bgColor: "#6a9cff",
    problemList: [],
  };

  const tagIdToIndex = new Map<number, number>();
  categorizedProblems.forEach((tag, index) => {
    tagIdToIndex.set(tag.bojTagId, index);
  });

  data.items.forEach((problem) => {
    let categorized = false;
    problem.tags.forEach((tag) => {
      const index = tagIdToIndex.get(tag.bojTagId);
      if (index !== undefined) {
        categorizedProblems[index].problemList.push(problem);
        categorized = true;
      }
    });
    if (!categorized) {
      uncategorizedProblems.problemList.push(problem);
    }
  });

  // Filter out tags with no problems
  let filteredCategorizedProblems = categorizedProblems.filter(
    (tag) => tag.problemList.length > 0
  );

  // Add the uncategorized problems category if it contains any problems
  if (uncategorizedProblems.problemList.length > 0) {
    filteredCategorizedProblems.push(uncategorizedProblems);
  }

  // If algorithmFilter is provided, filter the categorized problems based on the algorithmFilter
  if (algorithmFilter.length > 0) {
    filteredCategorizedProblems = filteredCategorizedProblems.filter((tag) =>
      algorithmFilter.includes(tag.kr)
    );
  }

  return filteredCategorizedProblems;
};
