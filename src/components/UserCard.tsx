const UserCard = ({
  user,
  onClick,
}: {
  user: string;
  onClick?: () => void;
}) => {
  return (
    <div
      onClick={onClick}
      className="w-[fit-content] h-userCard rounded-full bg-[#F4F4F4] px-4 py-2 flex items-center justify-center cursor-pointer"
    >
      <span className="text-[18px] text-[#a438f7a9]">{user}</span>
    </div>
  );
};
export default UserCard;
