import styles from './screenAboutMobile.module.css';
import Button from '../Button/Button';
import imagePhone from '../../images/phone.png';
import imagePhoneMobile from '../../images/phoneForMobile.png'



const ScreenAboutMobile = () => {
    return (
        <section id='mobilegame' className={styles.container}>
            <img src={imagePhone} className={styles.image} alt="Foto mobile phone"></img>
            <div className={styles.wrapperDescriptionMobileVersion}>
                <h1 className={styles.sectionName}>Мобильная версия</h1>
                <p className={styles.description}>Можно играть и на мобильном устройстве</p>
                <img src={imagePhoneMobile} className={styles.imageMobile} alt="Foto mobile phone"></img>
                <a className={styles.bottomLine} href='https://mosaic-rehab.ru:8443/' rel="noopener noreferrer" target='_blank'><Button className={styles.button} nameButton='Перейти'/></a>
                <Button className={styles.buttondisable} nameButton='Перейти'/>
                <h3 className={styles.infoDisabledButton}>Доступно на мобильном</h3>
            </div>
        </section>
    )
};

export default ScreenAboutMobile;