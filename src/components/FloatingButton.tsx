import HelpIcon from "../assets/Icons/helpIcon";

const FloatingButton = () => {
  return (
    <a
      className="fixed flex items-center justify-center w-16 h-16 rounded-full cursor-pointer right-4 bottom-4 bg-emerald-200 hover:shadow-md"
      href="https://moong23.notion.site/FAQ-SUP-5baa31f7ffd74a4a9a3fa6adf2e93971?pvs=4"
      target="_blank"
    >
      <HelpIcon
        width={42}
        fill="#000000"
      />
    </a>
  );
};

export default FloatingButton;
