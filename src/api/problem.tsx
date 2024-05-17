import axios from "axios";
import { ProbData, ProbFromApi } from "../interfaces";

interface IQueryKey {
  queryKey: [string, { userList: string[]; problemLevel?: [number, number] }];
}

export const getProblemList = async ({ queryKey }: IQueryKey) => {
  const [_key, { userList, problemLevel }] = queryKey;
  const response = await axios
    .get(
      "https://solved.ac/api/v3/search/problem?query=t@sup%20-@moonki0623&page=1"
    )
    .then((res) => {
      return res.data;
    })
    .catch((err) => {
      console.error(err);
    });
  return response as ProbFromApi;
};
