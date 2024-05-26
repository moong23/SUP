import { useEffect, useLayoutEffect, useState } from "react";
import UserCard from "./UserCard";

import { useUserList } from "../store";

const UserFilter = () => {
  const { userList, setUserList } = useUserList();

  const [localList, setLocalList] = useState<string[]>(
    JSON.parse(localStorage.getItem("userList") ?? "null") ?? []
  );

  const handleUserClick = (user: string) => {
    let newUserList = userList.filter((u) => u !== user);
    setLocalList(newUserList);
    setUserList(newUserList);
  };

  useLayoutEffect(() => {
    const localList = localStorage.getItem("userList");
    if (localList) {
      setLocalList(JSON.parse(localList));
    }
  }, []);

  useEffect(() => {
    console.log(userList);
    localStorage.setItem("userList", JSON.stringify(localList));
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

  const handleBlur = (e: React.FocusEvent<HTMLInputElement>) => {
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
    <div className="flex flex-col gap-4 mt-4 pb-12 mb-4 border-b border-b-[#cfcfcf]">
      <span className="flex flex-row w-full gap-4 overflow-scroll">
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
          className="focus:outline-none text-[18px] text-[#a438f7a9] cursor-text"
          onKeyDown={handleKeyDown}
          tabIndex={1}
          placeholder="BOJ 아이디를 입력하세요"
          onBlur={handleBlur}
        />
      </span>
      <details className="text-[#5B5B5B] font-medium text-base">
        <summary>주의사항</summary>* 스터디원의 백준 아이디를 쉼표, 스페이스바,
        엔터로 구분하여 넣어주세요 <br /> *{" "}
        <a
          href="https://solved.ac/"
          target="_blank"
          className="text-[#18CE3B]"
        >
          solved.ac
        </a>
        에 등록된 아이디에 한해서 검색이 가능합니다.
        <br /> * tab키를 누르거나, input이 blur될 때 문제를 검색합니다.
        <br />* 아이디를 클릭하면 삭제됩니다.
      </details>
    </div>
  );
};

export default UserFilter;
