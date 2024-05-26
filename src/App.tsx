import FloatingButton from "./components/FloatingButton";
import Header from "./components/Header";
import ProblemFilter from "./components/ProblemFilter";
import ProblemList from "./components/ProblemList";
import UserFilter from "./components/UserFilter";

function App() {
  return (
    <main className="flex flex-col mt-16 w-mainPage">
      <Header />
      <UserFilter />
      <ProblemFilter />
      <ProblemList />
      <FloatingButton />
    </main>
  );
}

export default App;
