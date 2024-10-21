import styles from './screenMain.module.css';
import Button from '../Button/Button';
import CastleSvg from '../CastleSvg/CastleSvg';


const ScreenMain = () => {
    return (
        <section className={styles.container}>
            <div className={styles.wrapperTopButtons}>
                <a className={styles.linkAncor} href='#gameplay'><Button className={styles.buttonGameplay} nameButton='Геймплей' ellipse={true}/></a>
                <a className={styles.linkAncor} href='#aboutgame'><Button className={styles.buttonAboutGame} nameButton='Об игре' ellipse={true}/></a>
            </div>
			<div className={styles.wrapperLogoAndButton}>
                <a href='https://batanandrei.github.io/bird-build-unity/' target="_blank"><Button className={styles.buttonLetsplay} nameButton='ИГРАТЬ'/></a>
                <div className={styles.logo}><CastleSvg/></div>
                <div className={styles.hiddenBlockForPosition}></div>
            </div>
		</section>
    )
};

export default ScreenMain;