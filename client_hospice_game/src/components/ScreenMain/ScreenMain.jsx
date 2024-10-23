import styles from './screenMain.module.css';
import Button from '../Button/Button';
//import video from '../../video/videoCastleGame2.0.mp4';


const ScreenMain = () => {
    return (
        <section id='main' className={styles.container}>
            <div className={styles.wrapperContext}>
                <div className={styles.wrapperInfoAndButton}>
                    <div className={styles.wrapperInfo}>
                        <h1 className={styles.title}>Построй, лечи, меняй<br/> жизни детей</h1>
                        <h2 className={styles.subTitle}>Представляем Замок Заботы! Симулятор детского реабилитационного центра!</h2>
                    </div>
                    <a className={styles.bottomLine} rel="noopener noreferrer" href='https://www.figma.com/design/wn8i34WXIVj03MoE4tyyBZ/%D0%97%D0%B0%D0%BC%D0%BE%D0%BA-%D0%B7%D0%B0%D0%B1%D0%BE%D1%82%D1%8B?node-id=0-1&node-type=canvas&t=YCW9gKxGRckBfqb3-0' target="_blank"><Button className={styles.button} nameButton='Играть'/></a>    
                </div>
                <div className={styles.wrapperVideo}>
                    <video poster="../../svg/backVideo" muted className={styles.videoPlayer} src='' controls>
                    </video>
                </div>
                <Button className={styles.buttonDisable} nameButton='Играть'/>
                <h3 className={styles.infoDisabledButton}>Работает на компьютере</h3>
            </div>
		</section>
    )
};

export default ScreenMain;