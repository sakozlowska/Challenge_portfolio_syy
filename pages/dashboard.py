from pages.base_page import BasePage


class Dashboard(BasePage):
    scouts_panel_header_xpath = "//header[contains(@class,'mui-fixed MuiPaper-elevation4')]"
    players_amount_text_xpath = "//div[text()='Ilość graczy']"
    games_amount_xpath = "//html/body/div/div/main/div/div/div/div[2]/b"
    logo_scouts_panel_xpath = "//div[@class='MuiCardMedia-root jss130']"
    link_dev_team_contact_xpath = "//a[starts-with(@href,'https://app.slack.com/client')]"
    text_add_player_xpath = "//span[text()='Dodaj gracza']"
    link_add_player_xpath = "//a[contains(@href,'pl/players/add')]"
    log_out_xpath = "//span[text()='Wyloguj']"
    left_panel_xpath = "//div[contains(@class,'Drawer-paperAnchorDockedLeft MuiPaper-elevation0')]"
    alex_molo_text_xpath = "//span[text()='Alex Molo']"

    pass

