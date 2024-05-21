import { useEffect, useRef } from "react";
import FilterIcon from "../assets/Icons/filterIcon.png";
import { getCategory } from "../utils/queryStringByProblemLevel";

interface FilterButtonProps {
  isOpen: boolean;
  text: string;
  children: React.ReactNode;
  value: string[] | number[] | number;
  type?: "level" | "algorithm" | "problemCnt";
  setValue: (value: any) => void;
  onClick: () => void;
}

const FilterButton = ({
  isOpen,
  text,
  children,
  value,
  type,
  setValue,
  onClick,
}: FilterButtonProps) => {
  const contentRef = useRef<HTMLSpanElement>(null);

  useEffect(() => {
    const handleClickOutside = (e: MouseEvent) => {
      if (
        contentRef.current &&
        !contentRef.current.contains(e.target as Node)
      ) {
        onClick();
      }
    };

    if (isOpen) {
      window.addEventListener("click", handleClickOutside);
    } else {
      window.removeEventListener("click", handleClickOutside);
    }

    return () => {
      window.removeEventListener("click", handleClickOutside);
    };
  }, [isOpen, onClick]);

  const handleContentClick = (e: React.MouseEvent<HTMLDivElement>) => {
    e.stopPropagation();
    onClick();
  };

  const handleChildrenClick = (e: React.MouseEvent<HTMLDivElement>) => {
    e.stopPropagation();
  };

  return (
    <span
      onClick={handleContentClick}
      ref={contentRef}
      className={`${
        isOpen
          ? "max-w-[240px] bg-red text-[#2582E1] border border-[#B2D1F4]"
          : "w-[fit-content] max-w-[240px] bg-white border border-[#DFDFDE] text-black"
      } relative rounded-full cursor-pointer transition-all duration-300 ease-in-out hover:bg-[#F9FBFE] hover:border-[#B2D1F4] hover:text-[#2582E1] `}
    >
      <span className="flex flex-row items-center w-full px-3 py-1 overflow-hidden text-ellipsis whitespace-nowrap">
        <img
          src={FilterIcon}
          alt="filterIcon"
          className="inline-block w-3 h-3 mr-3"
        />
        {text}
        {type === "level" && typeof value === "object" && (
          <>
            : {getCategory(value[0] as number)} ~{" "}
            {getCategory(value[1] as number)}
          </>
        )}
        {type === "algorithm" &&
          typeof value === "object" &&
          value.length > 0 && <>: {value.join(", ")}</>}
        {type === "problemCnt" && typeof value === "number" && value > 0 && (
          <>: {value}개</>
        )}
      </span>
      {isOpen && (
        <div
          className="cursor-default"
          onClick={handleChildrenClick}
        >
          {children}
        </div>
      )}
    </span>
  );
};

export default FilterButton;
