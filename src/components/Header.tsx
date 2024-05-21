import githubIcon from "../assets/Icons/githubIcon.png";
import { useState, useRef, useEffect } from "react";

const Header = () => {
  const timeoutRef = useRef<NodeJS.Timeout | null>(null);

  const handleMouseEnter = (e: React.MouseEvent<HTMLHeadingElement>) => {
    setIsHover(true);
  };

  const handleMouseLeave = (e: React.MouseEvent<HTMLHeadingElement>) => {
    timeoutRef.current = setTimeout(() => {
      setIsHover(false);
    }, 5000);
  };

  useEffect(() => {
    return () => {
      if (timeoutRef.current) {
        clearTimeout(timeoutRef.current);
      }
    };
  }, []);

  const [isHover, setIsHover] = useState<boolean>(false);
  return (
    <span className="flex flex-row justify-between w-full">
      <span className="flex flex-row w-full gap-8">
        {!isHover ? (
          <h1
            onMouseEnter={handleMouseEnter}
            className="w-[235px] text-[120px] font-bold cursor-pointer"
          >
            SUP
          </h1>
        ) : (
          <span
            onMouseLeave={handleMouseLeave}
            className="w-[235px] h-[180px] justify-evenly flex flex-col gap-2 px-4 shrink-0"
          >
            <span className="text-[32px] w-full items-center justify-between flex flex-row text-xl">
              Contact
              <a
                href="https://github.com/moong23"
                target="_blank"
                className="w-12 h-12 "
              >
                <img
                  src={githubIcon}
                  alt="githubIcon"
                  className="w-full h-full"
                />
              </a>
            </span>
            <span className="text-[32px] w-full items-center justify-between flex flex-row text-xl">
              Problem Set
              <a
                href="https://github.com/tony9402/baekjoon"
                target="_blank"
                className="w-12 h-12 "
              >
                <img
                  src={githubIcon}
                  alt="githubIcon"
                  className="w-full h-full"
                />
              </a>
            </span>
          </span>
        )}
        <section className="flex flex-col w-full gap-3">
          <span className="text-[32px]">Suggesting Unsolved Problems</span>
          <h4 className="text-[16px]">
            👋🏻 was<strong>sup</strong> 👋🏻
          </h4>
          <h4 className="text-[16px]">
            Welcome to <strong>SUP</strong>, where we <strong>sup</strong>port
            your journey to <em>conquer the unconquered!</em>
          </h4>
          <a
            href="https://forms.gle/R37kW7315rhCxPjE6"
            target="_blank"
            className="text-[16px] w-[fit-content] underline font-bold text-sky-600"
          >
            설문조사 및 피드백 링크
          </a>
        </section>
      </span>
    </span>
  );
};

export default Header;
