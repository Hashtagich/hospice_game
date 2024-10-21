import styles from './screenAboutGameplay.module.css';
import Slider from '../Slider/Slider';


const ScreenAboutGameplay = () => {



    return (
        <section id='gameplay' className={styles.container}>
            <div className={styles.wrapperDescriptionAndPlayer}>
                <h1 className={styles.sectionName}>ГЕЙМПЛЕЙ</h1>
                <p className={styles.description}>Процесс игры фокусируется на эффективном<br/> распределении ресурсов и принятии решений<br/> для обеспечения высокого качества реабилитации.</p>
                <video poster="../../images/imagePlayer.png" muted className={styles.videoPlayer} src="https://videos.pexels.com/video-files/1481903/1481903-sd_640_360_25fps.mp4" controls></video>
            </div>
            <div className={styles.wrapperSlider}>
                <div className={styles.slider}>
                    <Slider/>
                </div>
            </div>
        </section>
    )
};

export default ScreenAboutGameplay;