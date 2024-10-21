import styles from './screenAboutGame.module.css';
import Button from '../Button/Button';
import imageRealCenter from '../../images/imageRealCenter.png';
import imageRealCenterMobile from '../../images/imageRealCenterMobile.png';


const ScreenAboutGame = () => {
    return (
        <section id='aboutgame' className={styles.container}>
            <img src={imageRealCenter} className={styles.image} alt="Foto real center"/>
            <div className={styles.wrapperAboutGame}>
                <p className={styles.description}>Это игра-симулятор реального детского реабилитационного центра. Каждая покупка помогает настоящим детям. Игра основана на опыте действующего центра - создавая виртуальный, вы помогаете развивать реальный.</p>
                <img src={imageRealCenterMobile} className={styles.imageMobile} alt="Foto real center"/>
                <a href='https://detireb.ru/' rel="noopener noreferrer" target="_blank"><Button className={styles.button} nameButton='Мозайка'/></a>
            </div>
        </section>
    )
};

export default ScreenAboutGame;