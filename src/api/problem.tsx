import axios from "axios";
import { ProbData, ProbFromApi } from "../interfaces";
import { queryStringByUserList } from "../utils/queryStringByUserList";
import { queryStringByProblemLevel } from "../utils/queryStringByProblemLevel";
import { queryStringByProblemTags } from "../utils/queryStringByProblemTags";

interface IQueryKey {
  queryKey: [
    string,
    {
      userList: string[];
      problemLevel?: [number, number];
      problemTags?: string[];
    }
  ];
}

export const getProblemList = async ({ queryKey }: IQueryKey) => {
  const [_key, { userList, problemLevel, problemTags }] = queryKey;
  const userQuery = queryStringByUserList(userList);
  const levelQuery = queryStringByProblemLevel(problemLevel);
  const tagQuery = queryStringByProblemTags(problemTags as string[]);

  console.log(
    `https://solved.ac/api/v3/search/problem?query=${userQuery}${levelQuery}${tagQuery}&page=1&sort=random`
  );
  const response = await axios
    .get(
      `search/problem?query=${userQuery}${levelQuery}${tagQuery}&page=1&sort=random`
    )
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.error(err);
    });
  return response as ProbFromApi;
};
