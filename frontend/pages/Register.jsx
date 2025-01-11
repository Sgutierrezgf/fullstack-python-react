import { useForm } from "react-hook-form";
import { useAuth } from "../context/AuthContext";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

function RegisterPage() {
    const {
        register,
        handleSubmit,
        formState: { errors },
    } = useForm();
    const { signup, isAuthenticated } = useAuth();
    const navigate = useNavigate();

    useEffect(() => {
        if (isAuthenticated) navigate("/login");
    }, [isAuthenticated, navigate]);

    const onSubmit = handleSubmit(async (values) => {
        console.log(values);
        await signup(values);
    });

    return (
        <div className="container">
            <h1>Registro</h1>
            <form onSubmit={onSubmit}>
                <input
                    type="text"
                    {...register("first_name", { required: true })}
                    placeholder="Jhon"
                />
                {errors.first_name && <p className="error">First name is required</p>}
                <input
                    type="text"
                    {...register("last_name", { required: true })}
                    placeholder="Doe"
                />
                {errors.last_name && <p className="error">Last name is required</p>}
                <input
                    type="email"
                    {...register("email", { required: true })}
                    placeholder="example@example.com"
                />
                {errors.email && <p className="error">Email is required</p>}
                <input
                    type="number"
                    {...register("phone", { required: true })}
                    placeholder="30123665789"
                />
                {errors.phone && <p className="error">Phone is required</p>}
                <input
                    type="text"
                    {...register("gender", { required: true })}
                    placeholder="F or M"
                />
                {errors.gender && <p className="error">Gender is required</p>}
                <input
                    type="password"
                    {...register("password", { required: true })}
                    placeholder="Password"
                />
                {errors.password && <p className="error">Password is required</p>}
                <input
                    type="text"
                    {...register("role", { required: true })}
                    placeholder="admin or user"
                />
                {errors.role && <p className="error">Role is required</p>}
                <button type="submit">Registro</button>
            </form>
        </div>
    );
}

export default RegisterPage;