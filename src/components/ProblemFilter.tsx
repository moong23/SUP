import { useState } from "react";
import FilterButton from "./FilterButton";
import TagBox from "./TagBox";
import { Slider } from "@mui/material";
import { findTagIdByTagName } from "../utils/findTagIdByTagName";
import { getCategory } from "../utils/queryStringByProblemLevel";
import ProblemTag from "../assets/database/problemTag.json";
import closeIcon from "../assets/Icons/x.svg";
import { useFilterList } from "../store";

const ProblemFilter = () => {
  const [panel, setPanel] = useState({
    level: false,
    algorithm: false,
    problemCnt: false,
  });
  const [level, setLevel] = useState<[number, number]>([1, 20]);
  const [algorithm, setAlgorithm] = useState<string[]>([]);
  const [problemCnt, setProblemCnt] = useState<number>(50);
  const { setLevelFilter, setAlgorithmFilter, setProblemFilter } =
    useFilterList();

  // level slider
  const handleLevelChange = (event: Event, newValue: number | number[]) => {
    if (typeof newValue === "number") return;
    setLevel(newValue as [number, number]);
  };

  // algorithm tag
  const handleAlgorithmChange = (tagName: string) => {
    if (algorithm.includes(tagName)) {
      setAlgorithm(algorithm.filter((algo) => algo !== tagName));
    } else {
      setAlgorithm([...algorithm, tagName]);
    }
  };

  // problemCount slider
  const handleProblemCountChange = (
    event: Event,
    newValue: number | number[]
  ) => {
    if (typeof newValue !== "number") return;
    console.log(newValue);
    setProblemCnt(newValue);
  };

  // apply button
  const handleApplyBtnClick = () => {
    console.log(level, algorithm, problemCnt);
    setLevelFilter(level);
    setAlgorithmFilter(algorithm);
    setProblemFilter(problemCnt);
  };

  const valueText = (value: number) => {
    return `${getCategory(value)}`;
  };
  return (
    <div className="flex w-full mb-10">
      <div className="flex justify-between w-full h-full">
        <div className="flex w-full gap-2">
          <FilterButton
            isOpen={panel.level}
            text="난이도"
            value={level}
            setValue={setLevel}
            type="level"
            onClick={() =>
              setPanel({
                algorithm: false,
                problemCnt: false,
                level: !panel.level,
              })
            }
          >
            <div className="absolute flex flex-col top-9 w-[240px] bg-white shadow-xl border border-slate-200 rounded-lg px-4 py-4">
              <Slider
                min={1}
                max={20}
                value={level}
                getAriaValueText={valueText}
                onChange={handleLevelChange}
              />
            </div>
          </FilterButton>
          <FilterButton
            isOpen={panel.algorithm}
            text="알고리즘"
            value={algorithm}
            type="algorithm"
            setValue={setAlgorithm}
            onClick={() =>
              setPanel({
                level: false,
                problemCnt: false,
                algorithm: !panel.algorithm,
              })
            }
          >
            <div className="absolute flex flex-col top-9 w-[240px] h-[400px] bg-white shadow-xl border border-slate-200 rounded-lg px-2 py-4 text-black">
              <div className="w-full h-[fit-content] min-h-[40px] rounded-md bg-[#F7F7F5] shrink-0 flex flex-row flex-wrap gap-x-2 gap-y-2 py-2 px-2">
                {algorithm.map((algo, idx) => {
                  return (
                    <TagBox
                      key={idx}
                      tagName={algo}
                      tagId={findTagIdByTagName(algo) || -1}
                      onClick={() => handleAlgorithmChange(algo)}
                    >
                      <img
                        src={closeIcon}
                        alt="close"
                        className="w-4 h-4 ml-1"
                      />
                    </TagBox>
                  );
                })}
              </div>
              <div className="flex flex-col w-full gap-2 overflow-y-scroll ">
                {ProblemTag.map((tag, idx) => {
                  return (
                    <label
                      htmlFor={tag.kr}
                      key={idx}
                      className="flex items-center"
                    >
                      <input
                        type="checkbox"
                        id={tag.kr}
                        checked={algorithm.includes(tag.kr)}
                        className="mr-2"
                        onChange={() => handleAlgorithmChange(tag.kr)}
                      />
                      <TagBox
                        key={idx}
                        tagName={tag.kr}
                        tagId={tag.bojTagId}
                      />
                    </label>
                  );
                })}
              </div>
            </div>
          </FilterButton>
          <FilterButton
            isOpen={panel.problemCnt}
            text="문제 수"
            value={problemCnt}
            type="problemCnt"
            setValue={setProblemCnt}
            onClick={() =>
              setPanel({
                level: false,
                algorithm: false,
                problemCnt: !panel.problemCnt,
              })
            }
          >
            <div className="absolute top-9 w-[240px] bg-white shadow-xl border border-slate-200 rounded-lg px-4">
              <Slider
                min={0}
                max={50}
                value={problemCnt}
                onChange={handleProblemCountChange}
              />
            </div>
          </FilterButton>
        </div>
      </div>
      <div className="w-[100px] h-full shrink-0">
        <button
          className="w-full h-full bg-blue-400 rounded-md cursor-pointer"
          onClick={handleApplyBtnClick}
        >
          적용하기
        </button>
      </div>
    </div>
  );
};
export default ProblemFilter;
