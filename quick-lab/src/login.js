import './App.css';
import './login.css';
import React, { useState, useEffect } from 'react';
import { Link, useNavigate} from 'react-router-dom';
import myimage from './Images/Group 76.png'


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
            <div className='image-container'>
            <img src={myimage} alt="woman" width={450} />
            </div>
            <div className='form-container1'>
            <h3 className='heading'>LogIn To Your Account</h3>
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
                <p>Don't have an account? <span><Link style={{ color: '#00A9E5', textDecoration: 'inherit'}} to={'/'}>SignUp</Link></span></p>
            </div>
            </div>

        </div>
        </form>
    );
}
export default LoginForm;