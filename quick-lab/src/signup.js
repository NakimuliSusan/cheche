import './App.css';
import './signup.css';
import React, { useState, useEffect } from 'react';

function SignupForm() {
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [UserName, setUserName] = useState("");
    const [level, setLevel] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const handleSubmit = () => {
        const data = {
            firstName: firstName,
            lastName: lastName,
            userName: UserName,
            level: level,
            password: password,
            confirmPassword: confirmPassword
        }
        alert(data);
    }

    return (

        <form onSubmit={handleSubmit} >
            <div className='container'>
            <div class="firstname">
                <input type="firstName" name="firstName" required placeholder='First Name'
                    value={firstName}
                    onChange={(e) => { setFirstName(e.target.value) }}
                />
            </div>

            <div class="lastname">
                <input type="lastName" name="lastName" required placeholder='Last Name'
                    value={lastName}
                    onChange={(e) => { setLastName(e.target.value) }}
                />
            </div>

            <div class="username">
                <input type="userName" name="userName" required placeholder='userName'
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

            <div class="password">
                <input type="password" name="password" required placeholder='Password'
                    value={password}
                    onChange={(e) => { setPassword(e.target.value) }}
                />
            </div>

            <div class="confirmpassword">
                <input type="confirm password" name="confirm password" required placeholder='Confirm password'
                    value={password}
                    onChange={(e) => { setPassword(e.target.value) }}
                />
            </div>

            <div class="signupbtn">
                <button type='submit'>SignUp</button>
            </div>

            <div class="login">
                <p>Already have an account? <span>Login</span></p>
            </div>

        </div>

        </form>
    );
}
export default SignupForm;