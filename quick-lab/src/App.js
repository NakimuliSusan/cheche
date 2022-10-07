import './App.css';
import { BrowserRouter as Router, Route , Routes } from "react-router-dom";
import SignupForm from './signup';
import LoginForm from './login';



function App() {
  return (
    <div>
  <Router>
  <Routes>
        <Route path="/" element={<SignupForm/>}/>
        <Route path="/login" element={<LoginForm/>}/>
      
  </Routes>  

 </Router>
    {/* <SignupForm/> */}
    {/* <LoginForm/> */}
       
    </div>
  );
}

export default App;
