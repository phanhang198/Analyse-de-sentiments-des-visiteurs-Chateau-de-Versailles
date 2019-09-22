# -*- coding: utf-8 -*-

import time
import math

import numpy as np
import pandas as pd
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def generate_delay():
    mean = 3
    sigma = 0.8
    return np.random.normal(mean,sigma,1)[0]

def generate_delay_short():
    mean = 1
    sigma = 0.8
    return np.random.normal(mean,sigma,1)[0]

reviewNumberMax = 500
# TODO: To save comments in the go (step = 500 => every 500 comments)
step = 1000

chateaux = {
    'Vaux-le-Vicomte': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g660739-d246751-Reviews-Chateau_de_Vaux_le_Vicomte-Maincy_Seine_et_Marne_Ile_de_France.html',
        'categorie': []
    },
    'Fontainebleau': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g187145-d195894-Reviews-Chateau_de_Fontainebleau-Fontainebleau_Seine_et_Marne_Ile_de_France.html',
        'categorie': []
    },
    'Chenonceau': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g187123-d219171-Reviews-Chateau_de_Chenonceau-Chenonceaux_Indre_et_Loire_Centre_Val_de_Loire.html',
        'categorie': []
    },
    'Chambord': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g187121-d247337-Reviews-Chateau_de_Chambord-Chambord_Loir_et_Cher_Centre_Val_de_Loire.html',
        'categorie': []
    },
    'Amboise': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g187116-d230644-Reviews-Chateau_Royal_d_Amboise-Amboise_Indre_et_Loire_Centre_Val_de_Loire.html',
        'categorie': []
    },
    'Cheverny': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g616096-d242379-Reviews-Chateau_de_Cheverny-Cheverny_Loir_et_Cher_Centre_Val_de_Loire.html',
        'categorie': []
    },
    'Chantilly': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g227607-d246223-Reviews-Chateau_de_Chantilly-Chantilly_Oise_Hauts_de_France.html',
        'categorie': []
    },
    'Azay_le_Rideau': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g187117-d546899-Reviews-Chateau_of_Azay_le_Rideau-Azay_le_Rideau_Indre_et_Loire_Centre_Val_de_Loire.html',
        'categorie': []
    },
    'Villandry': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g187132-d546911-Reviews-Chateau_de_Villandry-Villandry_Indre_et_Loire_Centre_Val_de_Loire.html',
        'categorie': []
    },
    'Usse': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g1580983-d242380-Reviews-Chateau_d_Usse-Rigny_Usse_Indre_et_Loire_Centre_Val_de_Loire.html',
        'categorie': []
    },
    'Beynac': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g1079321-d266697-Reviews-Chateau_de_Beynac-Beynac_et_Cazenac_Dordogne_Nouvelle_Aquitaine.html',
        'categorie': []
    },
    'Blois': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g187119-d247336-Reviews-Chateau_Royal_de_Blois-Blois_Loir_et_Cher_Centre_Val_de_Loire.html',
        'categorie': []
    },
    'Koenigsbourg': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g2227211-d254489-Reviews-Chateau_du_Haut_Koenigsbourg-Orschwiller_Bas_Rhin_Grand_Est.html',
        'categorie': []
    },
    'Bretagne': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g187198-d230635-Reviews-Chateau_des_Ducs_de_Bretagne-Nantes_Loire_Atlantique_Pays_de_la_Loire.html',
        'categorie': []
    },
    'Pierrefonds': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g1029112-d1181824-Reviews-Chateau_de_Pierrefonds-Pierrefonds_Oise_Hauts_de_France.html',
        'categorie': []
    },
    'Angers': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g187197-d207132-Reviews-Chateau_d_Angers-Angers_Maine_et_Loire_Pays_de_la_Loire.html',
        'categorie': []
    },
    'Castelnaud': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g672395-d247692-Reviews-Chateau_de_Castelnaud-Castelnaud_la_Chapelle_Dordogne_Nouvelle_Aquitaine.html',
        'categorie': []
    },
    'Murol': {
        'url': 'https://www.tripadvisor.fr/Attraction_Review-g1016352-d3180991-Reviews-Chateau_de_Murol-Murol_Puy_de_Dome_Auvergne_Rhone_Alpes.html',
        'categorie': []
    },
}

browser = webdriver.Firefox()

for chateau in chateaux.keys():
    #browsermn = webdriver.Firefox(r'C:\Users\mnnguyen\Documents\SIMPLON\Machine Learning\Projet_NLP')
    
    if len(chateaux[chateau]['categorie']) > 0:
        #browser.get('https://www.tripadvisor.fr/Attraction_Review-g187148-d188681-Reviews-Palace_of_Versailles-Versailles_Yvelines_Ile_de_France.html')
        browser.get(chateaux[chateau]['url'])
        #moyen = browser.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[5]/div/div[1]/div[1]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div[3]/label').click()
        #mediocre = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/div[5]/div/div[1]/div[3]/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div[4]/label').click()

    for cat in chateaux[chateau]['categorie']:

        if cat == 0:
            categorieName = 'excellent' 
            labelName = 'Positive'
        elif cat == 1:
            categorieName = 'bon'
            labelName = 'Positive'
        elif cat == 2:
            categorieName = 'moyen'
            labelName = 'Negative'
        elif cat == 3:
            categorieName = 'mediocre'
            labelName = 'Negative'
        elif cat ==4:
            categorieName ='horrible'
            labelName = 'Negative'

        avis_list=[]
        date_list=[]
        url_list=[]
        reviewNumber = 0
        reviewNumberEnd = 0

        # TODO: Choix de la catégorie: Excellent, Très bien, Moyen, Médiocre, Horrible
        delay = generate_delay()
        time.sleep(delay)
        # categorie = browser.find_elements_by_class_name('row_label')[cat]
        # categorie.click()  
        # <div class="choices" data-param="trating" data-name="ta_rating">
        # <div class="ui_checkbox item" data-value="5" data-tracker="5">
        # <input id="filters_detail_checkbox_trating__5" type="checkbox" value="5" class="filters_detail_checkbox_trating_cbx" onchange="widgetEvCall('handlers.updateFilter', event, this);">
        # <label for="filters_detail_checkbox_trating__5" class="row_label label">Excellent</label><span class="row_bar_cell">
        choices = browser.find_elements_by_xpath("//div[@class='choices']") 
        eleList = choices[0].find_elements_by_tag_name('div')
        ui_checkbox = []
        for ele in eleList:
            # print(ele.get_attribute("class"))
            if ele.get_attribute("class") == 'ui_checkbox item':
                ui_checkbox.append(ele)
        # ui_checkbox = choices[0].find_elements_by_class_name('ui_checkbox item')
        ui_checkbox[cat].find_elements_by_tag_name('label')[0].click()

        # TODO: Expand the comment
        delay = generate_delay()
        time.sleep(delay)
        plus = browser.find_elements_by_xpath('//span[contains(@class,"taLnk ulBlueLinks")]') #pour click sur bouton Plus
        if len(plus) > 0:
            browser.execute_script("arguments[0].click();", plus[0])

        reviews = browser.find_elements_by_class_name('reviewSelector')

        suivantPossible = True
        pageNumber = browser.find_elements_by_xpath("//div[@class='pagination-details']/b")

        # while (i < len(reviews)) & (reviewNumberEnd < reviewNumberMax):
        while suivantPossible & (reviewNumberEnd < reviewNumberMax):
            delay = generate_delay()
            time.sleep(delay)

            for i in range(len(reviews)):
                
                pageNumber = browser.find_elements_by_xpath("//div[@class='pagination-details']/b")
                reviewNumber += 1
                reviewNumberEnd += 1
                if len(pageNumber)  > 2:
                    print('==============================Page %s - %s in %s=============================' % (pageNumber[0].text, pageNumber[1].text, pageNumber[2].text) )
                
                comment = browser.find_elements_by_xpath("//div[@class='ui_column is-9']")
                if len(comment[i].find_elements_by_tag_name("p")) > 0:
                    # avis = browser.find_elements_by_xpath("//div[@class='ui_column is-9']/div[@class='prw_rup prw_reviews_text_summary_hsx']")[0].find_elements_by_xpath("//p").text
                    # url = comment[i].find_elements_by_xpath("//div/a").get_attribute('href')
                    date = browser.find_elements_by_class_name('ratingDate')[i].get_attribute('title')
                    url = browser.find_elements_by_xpath("//div[@class='ui_column is-9']/div/a")[i].get_attribute('href')
                    avis = comment[i].find_elements_by_tag_name("p")[0].text

                    print(len(reviews), reviewNumber, date, avis)
                    print('===========================================================')
                    print(url)

                    avis_list.append(avis)
                    date_list.append(date)
                    url_list.append(url)

            if reviewNumberEnd >= step:
                df1 = pd.DataFrame(list(zip(avis_list,date_list,url_list)), columns=['Comments','Dates','URLs'])
                df1.insert(0,'Chateau',chateau)
                df1['Label'] = labelName
                # df1['Chateau'] = chateau
                # df1.to_csv(categorieName + '-' + str(reviewNumberStart) + '-' + str(reviewNumberEnd) + '.csv', index=False, encoding='utf-8')
                df1.to_csv('csv/' + categorieName + chateau + '-' + str(reviewNumberEnd) + '.csv', index=False, encoding='utf-8')
                reviewNumberStart = reviewNumberEnd + 1

            # TODO: Click next page
            # <div class="unified ui_pagination ">
            # <a data-page-number="4" data-offset="30" class="nav next taLnk ui_button primary" onclick="widgetEvCall('handlers.paginate', event, this); widgetEvCall('handlers.trackClick', event, this, 'pagination_next', '4');" href="/Attraction_Review-g187123-d219171-Reviews-or30-Chateau_de_Chenonceau-Chenonceaux_Indre_et_Loire_Centre_Val_de_Loire.html">Suivant</a>
            # <a class="nav next ui_button primary disabled">Suivant</a>
            # suivants = browser.find_elements_by_xpath('//*[@class="nav next taLnk ui_button primary"]')[0]
            delay = generate_delay()
            time.sleep(delay)
            ui_pagination = browser.find_elements_by_xpath("//div[@class='unified ui_pagination ']")
            if len(ui_pagination) > 0:
                eleList = ui_pagination[0].find_elements_by_tag_name('a')
                suivants = []
                suivantDisable = []
                for ele in eleList:
                    if ele.get_attribute("class") == 'nav next taLnk ui_button primary':
                        suivants.append(ele)
                    elif ele.get_attribute("class") == 'nav next ui_button primary disabled':
                        suivantDisable.append(ele)
                # suivantDisable = ui_pagination[0].find_elements_by_class_name('nav next ui_button primary disabled')
                # suivants = ui_pagination[0].find_elements_by_class_name('nav next taLnk ui_button primary')
                # print(len(ui_pagination), len(suivantDisable), len(suivants))
                if len(suivantDisable) > 0:
                    suivantPossible = False
                else:
                    suivants[0].click()

                    # TODO: Expand the comment
                    delay = generate_delay()
                    time.sleep(delay)
                    plus = browser.find_elements_by_xpath('//span[contains(@class,"taLnk ulBlueLinks")]')
                    # plus = browser.find_elements_by_xpath('//span[contains(@class,"taLnk ulBlueLinks")]')[0] #pour click sur bouton Plus
                    if len(plus) > 0:
                        browser.execute_script("arguments[0].click();", plus[0])

                    reviews = browser.find_elements_by_class_name('reviewSelector')
            else:
                suivantPossible = False
                
 
        df1 = pd.DataFrame(list(zip(avis_list,date_list,url_list)), columns=['Comments','Dates','URLs'])
        df1.insert(0,'Chateau',chateau)
        df1['Label'] = labelName
        df1.to_csv('csv/' + categorieName + chateau + '.csv', index=False, encoding='utf8')


