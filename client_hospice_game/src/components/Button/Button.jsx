const Button = ({ click, className, nameButton }) => {
    return (
        <button onClick={click} className={className}>{nameButton}</button>
    )
};

export default Button;