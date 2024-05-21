import { create } from "zustand";
import { ProbFromApi } from "../interfaces";
interface ZUserList {
  userList: string[];
  setUserList: (userList: string[]) => void;
}

export const useUserList = create<ZUserList>((set) => ({
  userList: ["moonki0623"],
  setUserList: (userList: string[]) => set({ userList }),
}));

interface ZFilterList {
  levelFilter: [number, number];
  algorithmFilter: string[];
  problemFilter: number;
  setLevelFilter: (levelFilter: [number, number]) => void;
  setAlgorithmFilter: (algorithmFilter: string[]) => void;
  setProblemFilter: (problemCnt: number) => void;
}

export const useFilterList = create<ZFilterList>((set) => ({
  levelFilter: [1, 20],
  algorithmFilter: [],
  problemFilter: 50,
  setLevelFilter: (levelFilter: [number, number]) => set({ levelFilter }),
  setAlgorithmFilter: (algorithmFilter: string[]) => set({ algorithmFilter }),
  setProblemFilter: (problemFilter: number) => set({ problemFilter }),
}));
