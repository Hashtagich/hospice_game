import styles from './screenMain.module.css';
import Button from '../Button/Button';


const ScreenMain = () => {

    return (
        <section className={styles.container}>
            <div className={styles.wrapperContext}>
                <div className={styles.wrapperInfoAndButton}>
                    <div className={styles.wrapperInfo}>
                        <h1 className={styles.title}>Построй, лечи, меняй<br/> жизни детей</h1>
                        <h2 className={styles.subTitle}>Представляем Замок Заботы! Симулятор<br/> детского реабилитационного центра!</h2>
                    </div>
                    <a href='https://batanandrei.github.io/bird-build-unity/' target="_blank"><Button className={styles.buttonLetsplay} nameButton='Играть'/></a>
                </div>
                <div className={styles.wrapperVideo}>
                    <video poster="../../images/imagePlayer.png" muted className={styles.videoPlayer} src="https://videos.pexels.com/video-files/1481903/1481903-sd_640_360_25fps.mp4" controls>
                    </video>
                    <div className={styles.svgPopugai}></div>
                </div>
            </div>
		</section>
    )
};

export default ScreenMain;