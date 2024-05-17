import { useQuery } from "@tanstack/react-query";
import { getProblemList } from "../api/problem";
import { useUserList } from "../store";
import { useEffect, useState } from "react";
import { ProbFromApi } from "../interfaces";
import ProblemTag from "../assets/database/problemTag.json";

const ProblemList = () => {
  const { userList } = useUserList();
  const { data, isLoading, error } = useQuery({
    queryKey: ["problemListbyFilters", { userList: userList }],
    queryFn: getProblemList,
    staleTime: 1000 * 60 * 5, // 5 min for now
  });

  const [problemList, setProblemList] = useState<ProbFromApi>({
    count: 0,
    items: [],
  });

  const preprocessProblemList = (data: ProbFromApi) => {
    const processedData = ProblemTag.map((tag) => {
      // tag를 기준으로 data를 필터링
    });
  };

  useEffect(() => {
    if (isLoading || !data) return;
    if (data.count === 0) return;
    if (error) {
      alert("관리자에게 문의하세요");
      return;
    }
    const processedData = preprocessProblemList(data);
    // setProblemList(processedData);
    console.log("preprocess", processedData);
    console.log("APIData", data);
  }, [isLoading, data, error]);

  return (
    <div>
      <span>ProblemList</span>
    </div>
  );
};

export default ProblemList;
