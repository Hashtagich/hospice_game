import styles from './theFooter.module.css';
import Button from '../Button/Button';


const TheFooter = () => {
    return (
        <footer className={styles.footer}>
			<div className={styles.container}>
				<div className={styles.wrapperLogoAndInfo}>
					<div className={styles.logoAndRu}>
						<div className={styles.logo}></div>
						<div className={styles.textRuAndGlobus}>
							<div className={styles.globusIcon}></div>
							<h4 className={styles.textRu}>Русский (RU)</h4>
						</div>
					</div>
					<div className={styles.policyInfo}>
						<h4 className={styles.textPolicy}>© Замок Заботы, 2024</h4>
						<h4 className={styles.textPolicy}>Конфиденциальность</h4>
						<h4 className={styles.textPolicy}>Условия</h4>
					</div>
				</div>
				<div className={styles.wrapperNavigationAndInfo}>
					<div className={styles.wrapperListsInfo}>
						<nav className={styles.listNavigationInfo}>
							<h2 className={styles.titleList}>Навигация</h2>
							<ul className={styles.ul}>
								<li className={styles.li}><a className={styles.linkAncor} href='#main'>Главная</a></li>
								<li className={styles.li}><a className={styles.linkAncor} href='#aboutgame'>Об игре</a></li>
								<li className={styles.li}><a className={styles.linkAncor} href='#featuresgame'>Особенности</a></li>
								<li className={styles.li}><a className={styles.linkAncor} href='#gameplay'>Геймплей</a></li>
								<li className={styles.li}><a className={styles.linkAncor} href='#mobilegame'>Мобильная версия</a></li>
							</ul>
						</nav>
						<div className={styles.listCommunityInfo}>
							<h2 className={styles.titleList}>Сообщество</h2>
							<div className={styles.wrapperItemComunity+' '+styles.addMarginTop}>
								<div className={styles.vkIcon}></div>
								<h3 className={styles.liComunity}>ВКонтакте</h3>
							</div>
							<div className={styles.wrapperItemComunity}>
								<div className={styles.telegaIcon}></div>
								<h3 className={styles.liComunity}>Телеграм</h3>
							</div>
							<div className={styles.wrapperItemComunity}>
								<div className={styles.facebookIcon}></div>
								<h3 className={styles.liComunity}>Facebook</h3>
							</div>
							<div className={styles.wrapperItemComunity}>
								<div className={styles.youtubeIcon}></div>
								<h3 className={styles.liComunity}>Youtube</h3>
							</div>
						</div>
						<div className={styles.listLinkInfo}>
							<h2 className={styles.titleList}>Для связи</h2>
							<div className={styles.wrapperItemLinks+' '+styles.addMarginTop}>
								<div className={styles.phoneFooterIcon}></div>
								<h3 className={styles.liComunity}>+7 988 380 31 41</h3>
							</div>
							<div className={styles.wrapperItemLinks}>
								<div className={styles.pismoFooterIcon}></div>
								<h3 className={styles.liComunity}>info.zamok_rehab@mail.ru</h3>
							</div>
							<div className={styles.wrapperItemLinks}>
								<div className={styles.pismoFooterIcon}></div>
								<h3 className={styles.liComunity}>help.zamok_rehab@mail.ru</h3>
							</div>
						</div>
					</div>
					<h4 className={styles.textPolicy+' '+styles.infoAboutGame}>Игра “Замок Заботы” является собственностью детского реабилитационно центра “Мозайка”</h4>
				</div>
			</div>
		</footer>
        )
};

export default TheFooter;