export const queryStringByUserList = (userList: string[]) => {
  if (userList.length === 0) return "t@sup";
  return "t@sup -@" + userList.join(" -@");
};
