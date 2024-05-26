import { useQuery } from "@tanstack/react-query";
import { getProblemList } from "../api/problem";
import { useFilterList, useUserList } from "../store";
import { useEffect, useState } from "react";
import { preprocessProblemList } from "../utils/sortApiProblemByTags";
import { CategorizedProblem } from "../interfaces";
import ProblemCard from "./ProblemCard";

const ProblemList = () => {
  const { userList } = useUserList();
  const { levelFilter, algorithmFilter, problemFilter } = useFilterList();
  const [problemList, setProblemList] = useState<CategorizedProblem[]>();

  const [noResult, setNoResult] = useState<boolean>(false);
  const { data, isLoading, error } = useQuery({
    queryKey: [
      "problemListbyFilters",
      {
        userList: userList,
        problemLevel: levelFilter,
        problemTags: algorithmFilter,
      },
    ],
    queryFn: getProblemList,
    staleTime: 1000 * 60 * 5, // 5 min for now
    refetchOnReconnect: false,
    refetchOnWindowFocus: false,
    refetchOnMount: false,
  });

  useEffect(() => {
    if (isLoading) return;

    if (error) {
      alert("관리자에게 문의하세요");
      return;
    }

    if (!data || data.count === 0) {
      setNoResult(true);
      return;
    }

    let filteredData = data;

    if (problemFilter) {
      filteredData = {
        ...data,
        items: data.items.slice(0, problemFilter),
      };
    }

    const processedData = preprocessProblemList(filteredData, algorithmFilter);
    console.log("processedData", processedData);
    setProblemList(processedData);
  }, [isLoading, data, error, problemFilter]);

  useEffect(() => {
    console.log(problemList);
  }, [problemList]);

  return !noResult && problemList ? (
    <div className="flex h-[600px] flex-row w-full gap-4 overflow-y-hidden shrink-0 overflow-w-scroll mb-12">
      {problemList?.map((problemByTag: CategorizedProblem) => {
        const tagBgColor = problemByTag.bgColor;
        return (
          <div
            key={problemByTag.bojTagId}
            className="flex flex-col overflow-w-scroll"
          >
            <span
              className="h-6 items-center justify-center w-[fit-content] flex px-3 py-1 mb-4 rounded-sm shrink-0 font-[500]"
              style={{ backgroundColor: tagBgColor }}
            >
              {problemByTag.kr}
            </span>
            <span className="flex flex-col w-full h-full gap-2 overflow-y-scroll">
              {problemByTag.problemList.map((problem) => {
                return (
                  <ProblemCard
                    currentTag={problemByTag.bojTagId}
                    key={problem.problemId + problemByTag.en}
                    probData={problem}
                  />
                );
              })}
            </span>
          </div>
        );
      })}
    </div>
  ) : noResult ? (
    <div>문제집에서 추천할 문제가 없어요!!!</div>
  ) : (
    <div>loading...</div>
  );
};

export default ProblemList;
