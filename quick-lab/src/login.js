import './App.css';
import './login.css';
import React, { useState, useEffect } from 'react';

function LoginForm() {
    const [userName, setUserName] = useState("");
    const [password, setPassword] = useState("");
    const handleSubmit = () => {
        const data = {
            userName: userName,
            password: password,
        }
        alert(data);
    }

    return (

        <form onSubmit={handleSubmit} >
            <div className='container'>
            <div class="username">
                <input type="userName" name="userName" required placeholder='Username'
                    value={userName}
                    onChange={(e) => { setUserName(e.target.value) }}
                />
            </div>

            <div class="password">
                <input type="password" name="password" required placeholder='Password'
                    value={password}
                    onChange={(e) => { setPassword(e.target.value) }}
                />
            </div>

            <div class="forgot">
                <p> Forgot password?</p>
            </div>

            <div class="loginbtn">
                <button type='submit'>Login</button>
            </div>

            <div class="signup">
                <p>Don't have an account?  <span> Signup</span></p>
            </div>

        </div>
        </form>
    );
}
export default LoginForm;