import './signup.css';
import React, { useState, useEffect } from 'react';
import { Link, useNavigate} from 'react-router-dom';
import myimage from './Images/Group 76.png'
import * as Yup from 'yup'

function SignupForm() {
    const navigate = useNavigate()
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [UserName, setUserName] = useState("");
    const [level, setLevel] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const handleSubmit = (e) => {
        e.preventDefault();
        navigate("/login")
        if(this.validate()){
            console.log(this.state);
      
            let input = {};
            input["name"] = "";
            input["email"] = "";
            input["password"] = "";
            input["confirm_password"] = "";
            this.setState({input:input});
      
            alert('Demo Form is submited');
        }
    }

      
    const  validate =() =>{
          let input = this.state.input;
          let errors = {};
          let isValid = true;
      
          if (!input["name"]) {
            isValid = false;
            errors["name"] = "Please enter your name.";
          }
      
          if (!input["email"]) {
            isValid = false;
            errors["email"] = "Please enter your email Address.";
          }
      
          if (typeof input["email"] !== "undefined") {
              
            var pattern = new RegExp(/^(("[\w-\s]+")|([\w-]+(?:\.[\w-]+)*)|("[\w-\s]+")([\w-]+(?:\.[\w-]+)*))(@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][0-9]\.|1[0-9]{2}\.|[0-9]{1,2}\.))((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\.){2}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[0-9]{1,2})\]?$)/i);
            if (!pattern.test(input["email"])) {
              isValid = false;
              errors["email"] = "Please enter valid email address.";
            }
          }
      
          if (!input["password"]) {
            isValid = false;
            errors["password"] = "Please enter your password.";
          }
      
          if (!input["confirm_password"]) {
            isValid = false;
            errors["confirm_password"] = "Please enter your confirm password.";
          }
      
          if (typeof input["password"] !== "undefined" && typeof input["confirm_password"] !== "undefined") {
              
            if (input["password"] !== input["confirm_password"]) {
              // eslint-disable-next-line no-unused-vars
              isValid= false;
              errors["password"] = "Passwords don't match.";
            }
          } 
      
          this.setState({
            errors: errors
          });
      
      }
    return (

        <form onSubmit={handleSubmit} >
            <div className='container'>
            <div className='image-container'>
            <img src={myimage} alt="woman" width={450} />
            </div>
            <div className='form-container'>
            <h3 className='headings'>Create an Account</h3>
            <div class="firstname">
                <input type="firstName" name="firstName" required placeholder='First Name'
                    value={firstName}
                    onChange={(e) => {setFirstName(e.target.value) }}
                />
            </div>

            <div class="lastname">
                <input type="lastName" name="lastName" required placeholder='Last Name'
                    value={lastName}
                    onChange={(e) => { setLastName(e.target.value) }}
                />
            </div>

            <div class="username-1">
                <input type="userName" name="userName" required placeholder='UserName'
                    value={UserName}
                    onChange={(e) => { setUserName(e.target.value) }}
                />
            </div>
            <div class="level">
                <input type="level" name="level" required placeholder='Level'
                    value={level}
                    onChange={(e) => { setLevel(e.target.value) }}
                />
            </div>

            <div class="password-1">
                <input type="password" name="password" required placeholder='Password'
                    value={password}
                    onChange={(e) => {setPassword(e.target.value) }}
                />
            </div>

            <div class="confirmpassword">
                <input type="password" name="confirm password" required placeholder='Confirm password'
                    value={confirmPassword}
                    onChange={(e) => {setConfirmPassword(e.target.value) }}
                />
            </div>

            <div class="signupbtn">
                <button type='submit'>SignUp</button>
            </div>

            <div class="login">
                <p>Already have an account? <span><Link style={{ color: '#00A9E5', textDecoration: 'inherit'}} to={'/login'}>Login</Link></span></p>
            </div>
        </div>
        </div>

        </form>
    );
}
export default SignupForm;