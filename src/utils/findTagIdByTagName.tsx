import ProblemTag from "../assets/database/problemTag.json";

export const findTagIdByTagName = (tagName: string) => {
  return ProblemTag.find((tag) => tag.kr === tagName)?.bojTagId ?? -1;
};
