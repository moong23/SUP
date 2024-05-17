import { useEffect, useState } from "react";
import UserCard from "./UserCard";
import { getProblemList } from "../api/problem";
import { useProblemList, useUserList } from "../store";
import { useQuery } from "@tanstack/react-query";

const UserFilter = ({ initialProps }: { initialProps?: string[] }) => {
  const { setProblemList } = useProblemList();

  // const [userList, setUserList] = useState(
  //   initialProps ?? ["moonki0623", "moong23"]
  // );
  const { userList, setUserList } = useUserList();

  const [localList, setLocalList] = useState<string[]>(
    initialProps ?? ["moonki0623", "moong23"]
  );
  const handleUserClick = (user: string) => {
    let newUserList = userList.filter((u) => u !== user);
    setLocalList(newUserList);
  };

  useEffect(() => {
    console.log(userList);
  }, [userList]);

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" || e.key === "," || e.key === " ") {
      e.preventDefault();
      const value = e.currentTarget.value.trim();
      if (value.length < 3) {
        alert("ID must be at least 3 characters long");

        return;
      }
      if (value) {
        console.log("adding new user");
        addNewUser(value);
        e.currentTarget.value = "";
      }
    }
  };

  const handleBlur = (e: any) => {
    const value = e.target.value.trim();
    // will handle api fetching event in here.
    if (0 < value.length && value.length < 3) {
      alert("ID must be at least 3 characters long");
      e.target.value = "";
      return;
    }
    if (value) {
      addNewUser(value);
    }
    if (value in localList || value === "") {
      setUserList(localList);
    } else {
      setUserList([...localList, value]);
    }
    e.target.value = "";
  };

  const addNewUser = (user: string) => {
    if (localList.includes(user)) return; // Prevents duplicate users
    const newUserList = [...localList, user];
    setLocalList(newUserList);
  };
  return (
    <div className="flex flex-col gap-4 mt-10 pb-12 mb-4 border-b border-b-[#cfcfcf]">
      <span className="flex flex-row w-full gap-4">
        {localList.map((user: string) => {
          return (
            <UserCard
              key={user}
              user={user}
              onClick={() => handleUserClick(user)}
            />
          );
        })}
        <input
          type="text"
          className="focus:outline-none text-[18px] text-[#a438f7a9]"
          onKeyDown={handleKeyDown}
          placeholder="BOJ 아이디를 입력하세요"
          onBlur={handleBlur}
        />
      </span>
      <span className="text-[#5B5B5B] font-medium text-base">
        * 스터디원의 백준 아이디를 쉼표, 스페이스바, 엔터로 구분하여 넣어주세요{" "}
        <br /> * input이 blur될 때 문제를 검색합니다.
      </span>
    </div>
  );
};

export default UserFilter;
