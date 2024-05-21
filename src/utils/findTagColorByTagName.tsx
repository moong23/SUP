import ProblemTag from "../assets/database/problemTag.json";

export const findTagColorByTagName = (bojTagId: number): string => {
  return (
    ProblemTag.find((tag) => tag.bojTagId === bojTagId)?.bgColor ?? "#6a9cff"
  );
};
