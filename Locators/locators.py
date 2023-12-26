class orangehrm_xpaths:
    username_input_box = "//input[@name='username']"
    password_input_box = "//input[@name='password']"
    login_submit = "//button[@type='submit']"
    logout_dropdown = "//p[@class='oxd-userdropdown-name']"
    logout_button = "//a[text()='Logout']"
    invalid_cred = "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]"
    PIM_tab = "//ul[@class='oxd-main-menu']/li[2]/a"
    save_buuton = "//button[@type='submit']"
    forgot_password = "//div[@class='orangehrm-login-forgot']/p"
    reset_username_input = "//input[normalize-space(@class)='oxd-input oxd-input--active']"
    reset_password_button = "//button[contains(normalize-space(@class),'orangehrm-forgot-password-button--reset')]"
    reset_password_successful = "//h6[contains(normalize-space(@class),'orangehrm-forgot-password-title')]"
    admin_tab = "(//a[normalize-space(@class='oxd-main-menu-item')])[2]"
    admin_header_options = "//nav[normalize-space(@class='oxd-topbar-body-nav')]/ul/li"
    main_menu_options = "//ul[@class='oxd-main-menu']/li"
    cancel_button = "//button[@type='button']"