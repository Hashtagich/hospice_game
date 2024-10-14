import styles from './screenAboutRealCenter.module.css';
import Button from '../Button/Button';


const ScreenAboutRealCenter = () => {
    return (
        <section id='realcenter' className={styles.container}>
            <div className={styles.wrapperDescriptionAndButton}>
                <h1 className={styles.nameSection}>Детский Реабилитацонный<br/>Центр «Мозайка»</h1>
                <p className={styles.descriptionAboutMazaika}>Вы можете помочь реальным детям даже не заходя в игру</p>
                <a href='https://detireb.ru/' rel="noopener noreferrer" target='_blank'><Button className={styles.button} nameButton='Помочь'/></a>
            </div>
            <div className={styles.wrapperCenterLogoSvg}></div>
        </section>
    )
};

export default ScreenAboutRealCenter;