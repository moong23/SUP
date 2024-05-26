export interface ProbData {
  problemId: number;
  titles: Title[];
  level: number;
  tags: Tag[];
}

export interface ProbFromApi {
  count: number;
  items: ProbItem[];
}

export interface ProbItem {
  acceptedUserCount?: number;
  averageTries?: number;
  givesNoRating?: boolean;
  isLevelLocked?: boolean;
  isPartial?: boolean;
  isSolvable?: boolean;
  level: number;
  metadata?: any;
  official?: boolean;
  problemId: number;
  sprout?: boolean;
  tags: Tag[];
  titleKo: string;
  titles?: Title[];
  votedUserCount?: number;
}
export interface Tag {
  aliases: Alias[];
  bojTagId: number;
  displayNames: DisplayName[];
  isMeta: boolean;
  key: string;
}

interface Alias {
  alias: string;
}

interface DisplayName {
  language: string;
  name: string;
  short: string;
}
interface Title {
  isOriginal: boolean;
  language: string;
  languageDisplayName: string;
  title: string;
}

export interface CategorizedProblem {
  kr: string;
  en: string;
  bojTagId: number;
  bgColor: string;
  problemList: ProbItem[];
}

export interface IconProps {
  width: number;
  height?: number;
  fill?: string;
  className?: string;
  onClick?: () => void;
}
