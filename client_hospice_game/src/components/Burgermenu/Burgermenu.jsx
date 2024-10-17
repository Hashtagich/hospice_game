import styles from './burgermenu.module.css';


const Burgermenu = ({ headerColor, closeBurger }) => {
    return (
        <div className={headerColor ? styles.containerLight : styles.container}>
            <ul className={styles.listnavigation}>
				<li className={styles.li}><a className={styles.linkAncor} onClick={closeBurger} href='#aboutgame'>Об игре</a></li>
				<li className={styles.li}><a className={styles.linkAncor} onClick={closeBurger} href='#featuresgame'>Особенности</a></li>
				<li className={styles.li}><a className={styles.linkAncor} onClick={closeBurger} href='#gameplay'>Геймплей</a></li>
                <li className={styles.li}><a className={styles.linkAncor} onClick={closeBurger} href='#mobilegame'>Мобильная версия</a></li>
				<li className={styles.li}><a className={styles.linkAncor} onClick={closeBurger} href='#realcenter'>РЦ "Мозайка"</a></li>
			</ul>
            <div className={styles. listIconsLink}>
                <div className={styles.vkIcon}></div>
                <div className={styles.telegaIcon}></div>
                <div className={styles.facebookIcon}></div>
                <div className={styles.youtubeIcon}></div>
            </div>
        </div>
    )
};

export default Burgermenu;