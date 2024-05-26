import { ProbItem } from "../interfaces";
import { findTagColorByTagName } from "../utils/findTagColorByTagName";
import TagBox from "./TagBox";

const ProblemCard = ({
  probData,
  currentTag,
}: {
  probData: ProbItem;
  currentTag: number;
}) => {
  return (
    <a
      href={`https://www.acmicpc.net/problem/${probData.problemId}`}
      target="_blank"
      className="px-4 py-3 shrink-0 bg-white border border-[#bababa] rounded-lg cursor-pointer w-card h-card shadow-sm hover:shadow-lg transition duration-300 ease-in-out"
    >
      <div className="flex items-center justify-between">
        <div className="flex items-center">
          <img
            loading="lazy"
            src={require(`../assets/Icons/problemLevel/${probData.level}.svg`)}
            alt={`difficulty-${probData.level}`}
            className="w-6 h-6"
          />

          <div className="w-full ml-2 overflow-hidden text-lg whitespace-nowrap text-ellipsis">
            {probData.problemId}. {probData.titleKo}
          </div>
        </div>
      </div>

      <div className="flex w-full gap-2 mt-4 overflow-x-hidden">
        {probData.tags.map((tag, idx) => (
          <TagBox
            key={idx}
            tagId={tag.bojTagId}
            tagName={tag.displayNames[0].name}
            currentTag={currentTag}
          />
        ))}
      </div>
    </a>
  );
};

export default ProblemCard;
