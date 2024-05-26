import { findTagColorByTagName } from "../utils/findTagColorByTagName";
import { findTagIdByTagName } from "../utils/findTagIdByTagName";

interface TagBoxProps {
  tagName: string;
  tagId?: number;
  currentTag?: number;
  children?: React.ReactNode;
  onClick?: () => void;
}

const TagBox = ({
  tagName,
  tagId,
  currentTag,
  children,
  onClick,
}: TagBoxProps) => {
  tagId = tagId || findTagIdByTagName(tagName);
  const bgColor = findTagColorByTagName(tagId);
  return (
    <div
      style={{ backgroundColor: bgColor }}
      onClick={onClick}
      className={`${
        currentTag === tagId ? "order-first" : ""
      } h-6 items-center justify-center w-[fit-content] flex px-3 py-1 rounded-sm shrink-0 cursor-pointer`}
    >
      {tagName}
      {children}
    </div>
  );
};

export default TagBox;
