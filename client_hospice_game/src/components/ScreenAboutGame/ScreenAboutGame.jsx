import styles from './screenAboutGame.module.css';
import Button from '../Button/Button';


const ScreenAboutGame = () => {
    return (
        <section id='aboutgame' className={styles.container}>
            <img className={styles.image}/>
            <div className={styles.wrapperAboutGame}>
                <p className={styles.description}>Это игра-симулятор реального детского реабилитационного центра. Каждая покупка помогает настоящим детям. Игра основана на опыте действующего центра - создавая виртуальный, вы помогаете развивать реальный.</p>
                <a href='https://detireb.ru/' target="_blank"><Button className={styles.button} nameButton='Мозайка'/></a>
            </div>
        </section>
    )
};

export default ScreenAboutGame;