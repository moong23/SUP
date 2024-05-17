import "./App.css";
import Header from "./components/Header";
import ProblemArea from "./components/ProblemArea";
import ProblemList from "./components/ProblemList";
import UserFilter from "./components/UserFilter";

function App() {
  return (
    <main className="flex flex-col mt-16 w-mainPage">
      <Header />
      <UserFilter />
      <ProblemArea />
    </main>
  );
}

export default App;
