export const getCategory = (level: number) => {
  const categories = ["b", "s", "g", "p", "d", "r"];
  const categoryIndex = Math.floor((level - 1) / 5);
  const indexInCategory = 5 - ((level - 1) % 5);
  return `${categories[categoryIndex]}${indexInCategory}`;
};

export const queryStringByProblemLevel = (
  problemLevel: [number, number] | unknown
): string => {
  if (typeof problemLevel !== "object" || !Array.isArray(problemLevel)) {
    return "";
  }
  const [start, end] = problemLevel;

  if (start < 1 || end > 30 || start > end) {
    throw new Error("Invalid problem level range");
  }

  const startLevel = getCategory(start);
  const endLevel = getCategory(end);

  return `%20*${startLevel}..${endLevel}`;
};
