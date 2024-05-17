import { create } from "zustand";
import { ProbFromApi } from "../interfaces";

interface ZProblemList {
  problemList: ProbFromApi;
  setProblemList: (problemList: ProbFromApi) => void;
}

export const useProblemList = create<ZProblemList>((set) => ({
  problemList: { count: 0, items: [] },
  setProblemList: (problemList: ProbFromApi) => set({ problemList }),
}));

interface ZUserList {
  userList: string[];
  setUserList: (userList: string[]) => void;
}

export const useUserList = create<ZUserList>((set) => ({
  userList: ["moonki0623"],
  setUserList: (userList: string[]) => set({ userList }),
}));
