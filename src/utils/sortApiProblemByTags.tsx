import ProblemTag from "../assets/database/problemTag.json";
import { ProbFromApi, CategorizedProblem } from "../interfaces";

// Define the structure for the return type

export const preprocessProblemList = (
  data: ProbFromApi
): CategorizedProblem[] => {
  // Initialize the result array based on ProblemTag
  const categorizedProblems: CategorizedProblem[] = ProblemTag.map((tag) => ({
    kr: tag.kr,
    en: tag.en,
    bojTagId: tag.bojTagId,
    bgColor: tag.bgColor,
    problemList: [],
  }));

  // Add an additional category for uncategorized problems
  const uncategorizedProblems: CategorizedProblem = {
    kr: "기타",
    en: "miscellaneous",
    bojTagId: -1, // Using -1 or any other unique value to represent uncategorized problems
    bgColor: "#6a9cff",
    problemList: [],
  };

  // Create a mapping from bojTagId to the index in the categorizedProblems array
  const tagIdToIndex = new Map<number, number>();
  categorizedProblems.forEach((tag, index) => {
    tagIdToIndex.set(tag.bojTagId, index);
  });

  // Iterate over each problem in the API data
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
  const filteredCategorizedProblems = categorizedProblems.filter(
    (tag) => tag.problemList.length > 0
  );

  // Add the uncategorized problems category if it contains any problems
  if (uncategorizedProblems.problemList.length > 0) {
    filteredCategorizedProblems.push(uncategorizedProblems);
  }

  return filteredCategorizedProblems;
};
