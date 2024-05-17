import { ProbData } from "../interfaces";

const ProblemCard = async ({ probData }: { probData: ProbData }) => {
  return (
    <a
      href={`https://www.acmicpc.net/problem/${probData.problemId}`}
      target="_blank"
      className="px-4 py-5 bg-white border border-red-200 rounded-lg cursor-pointer w-card h-card"
    >
      <div className="flex justify-between">
        <div className="flex items-center">
          <img
            loading="lazy"
            src={`https://static.solved.ac/tier_small/${probData.level}.svg`}
            alt="difficulty"
            width={24}
            height={24}
          />

          <div className="ml-2 text-lg">
            {probData.problemId}. {probData.titles[0].title}
          </div>
        </div>
      </div>
      <div className="mt-4">
        {probData.tags.map((tag, idx) => (
          <div
            key={idx}
            className="inline-block px-2 py-1 mr-2 text-sm bg-gray-200 rounded-lg"
          >
            {tag.displayNames[0].name}
          </div>
        ))}
      </div>
    </a>
  );
};

export default ProblemCard;
