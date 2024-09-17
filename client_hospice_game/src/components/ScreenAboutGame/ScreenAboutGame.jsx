import styles from './screenAboutGame.module.css';
import Button from '../Button/Button';


const ScreenAboutGame = () => {
    return (
        <section id='aboutgame' className={styles.container}>
            <div className={styles.wrapperRealCenterFoto}>
                <img className={styles.image}/>
                <h2 className={styles.descriptionFotoCenter}>Реальный центр</h2>
            </div>
            <div className={styles.wrapperAboutGame}>
                <div className={styles.descriptionGame}>
                    <h1 className={styles.nameSection}>ЦЕЛЬ ИГРЫ</h1>
                    <p className={styles.description}>Это игра в жанре «стратегия», где игрок должен нанимать персонал, обустраивать помещения, закупать оборудование  и организовывать эффективную работу центра для оказания помощи детям с ограниченными возможностями.</p>
                </div>
                <div className={styles.fotoAndButtonGame}>
                    <div>
                        <img className={styles.fotoGame}/>
                        <h2 className={styles.descriptionFotoGame}>ИГРА</h2>
                    </div>
                    <a href='https://batanandrei.github.io/bird-build-unity/' target="_blank"><Button className={styles.button} nameButton='К ИГРЕ'/></a>
                </div>
            </div>
        </section>
    )
};

export default ScreenAboutGame;