import Header from "./components/Header";
import ProblemArea from "./components/ProblemArea";
import ProblemFilter from "./components/ProblemFilter";
import ProblemList from "./components/ProblemList";
import UserFilter from "./components/UserFilter";

function App() {
  return (
    <main className="flex flex-col mt-16 w-mainPage">
      <Header />
      <UserFilter />
      <ProblemFilter />
      <ProblemArea />
      {/* <div className="w-full h-4 bg-red-200 shrink-0 footer"></div> */}
    </main>
  );
}

export default App;
