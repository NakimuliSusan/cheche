import './signup.css';
// import Footer from './Footer';
import React, { useState, useEffect } from 'react';
import { Link, useNavigate} from 'react-router-dom';
import myimage from './Images/Group 76.png'
import { FaLock } from "react-icons/fa";
import { AiFillLayout} from "react-icons/ai";
import { BsPersonFill } from "react-icons/bs";
import { yupResolver } from "@hookform/resolvers/yup";
import { useForm } from "react-hook-form";
import * as yup from 'yup';


function SignupForm() {
    const navigate = useNavigate()
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [UserName, setUserName] = useState("");
    const [level, setLevel] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");

    const formSchema = yup.object().shape({
        firstName: yup.string().required('First name is required'),
        lastName: yup.string().required('Last name is required'),
        UserName: yup.string().required(),
        level: yup.string().required('enter level'),
        password: yup.string().min(8).max(15).required(),
        confirmPassword: yup.string().oneOf([yup.ref("password"), null]),
      })


const { register, handleSubmit, formState: { errors }, reset } = useForm({
        resolver: yupResolver(formSchema),
      });
     
const onSubmitHandler = () => {
    //    e.preventDefault();
       navigate("/login")
       reset();
    }
// const submitting=()=>{
//     if(!errors){
//         navigate("/login")

//     }
// }

    // onClick={() => {navigate('/login');}}
     
    return (

        <form onSubmit={handleSubmit(onSubmitHandler)} >
            <div className='container'>
            <div className='image-container'>
            <img src={myimage} alt="woman" width={450} />
            </div>
            <div className='form-container'>
            <h3 className='headings'>Create an Account</h3>
            <div class="firstname-1">
            <div className='icons'>
                   <BsPersonFill/>
                </div>
                <div class="firstname">
                <input type="firstName" name="firstname" required placeholder='First Name'
                        {...register("firstName")}
                    onChange={(e) => {setFirstName(e.target.value) }}    
                />
                {errors.firstName?.message}
                </div>  
            </div>

            <div class="lastname-1">
                <div className='icons'>
                   <BsPersonFill/>
                </div>
                <div className='lastname'>
                <input type="lastName" name="lastname" required placeholder='Last Name'
                       {...register("lastName")}
                    onChange={(e) => {setLastName(e.target.value) }}
                />
                <i>{errors.lastName?.message}</i>
                </div>
            </div>

            <div class="username1">
            <div className='icons'>
                   <BsPersonFill/>
                </div>
            <div className="username-1">
                <input  type="userName" name="userName" required placeholder='UserName'
                       {...register("UserName")}
                    onChange={(e) => { setUserName(e.target.value) }}
                />
                {errors.UserName?.message}
                </div>
            </div>
            <div class="level-1">
            <div className='icons'>
                   <AiFillLayout/>
                </div>
                <div className='level'>
                <input  type="level" name="level" required placeholder='Level'
                      {...register("level")}
                    onChange={(e) => { setLevel(e.target.value) }}
                />
                {errors.level?.message}
                </div>
            </div>

            <div class="password">
             <div className='icons'>
             <FaLock />
            </div>  
            <div class="password-1"> 
               <input type="password" name="password"  required  placeholder=' Password'
                       {...register("password")}
                    onChange={(e) => {setPassword(e.target.value) }}
                />
                 <i>{errors.password?.message}</i>
                </div>
            </div>

            <div class="confirmpassword-1">
            <div className='icons'>
             <FaLock />
            </div> 
            < div className="confirmpassword">
                <input  type="password" name="confirm password" required placeholder='Confirm password'
                      value={confirmPassword}
                    onChange={(e) => {setConfirmPassword(e.target.value) }}
                />
                </div>
                {errors.confirmPassword}
            </div>
            

            <div class="signupbtn">
            <button onClick={ !errors &&  navigate("/login")} type="submit">SignUp</button>
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