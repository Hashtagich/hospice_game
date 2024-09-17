import EllipsGreySvg from '../EllipsGreySvg/EllipsGreySvg';


const Button = ({ className, nameButton, ellipse }) => {
    return (
        <button className={className}>
                {ellipse && <EllipsGreySvg/>}
                {nameButton}
            </button>
    )
};

export default Button;