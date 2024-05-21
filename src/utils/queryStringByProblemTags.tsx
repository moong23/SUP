import ProblemTag from "../assets/database/problemTag.json";

interface Tag {
  kr: string;
  en: string;
  bojTagId: number;
  bgColor: string;
}

export const queryStringByProblemTags = (problemTags: string[]): string => {
  if (!problemTags || problemTags.length === 0) return "";

  const tagMap = (ProblemTag as Tag[]).reduce((acc, tag) => {
    acc[tag.kr] = tag.en;
    return acc;
  }, {} as Record<string, string>);

  const englishTags = problemTags.map((tag) => `%23${tagMap[tag]}`).join("|");

  return `%20(${englishTags})`;
};
