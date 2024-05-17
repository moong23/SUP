import githubIcon from "../assets/Icons/githubIcon.png";
import velogIcon from "../assets/Icons/velogIcon.png";
import kakaoIcon from "../assets/Icons/kakaoIcon.png";

const Header = () => {
  return (
    <span className="flex flex-row justify-between w-full">
      <span className="flex flex-row w-full gap-8">
        <h1 className="text-[160px] font-bold">SUP</h1>
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
          <span className="flex flex-row gap-6 mt-6">
            <a
              href="https://github.com/moong23"
              target="_blank"
            >
              <img
                src={githubIcon}
                alt="githubIcon"
                width={48}
                height={48}
              />
            </a>
            <img
              src={velogIcon}
              alt="velogIcon"
              width={48}
              height={48}
            />
            <img
              src={kakaoIcon}
              alt="kakaoIcon"
              width={48}
              height={48}
            />
          </span>
        </section>
      </span>
    </span>
  );
};

export default Header;
