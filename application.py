import streamlit as st
import pickle
import pandas as pd
sim = pickle.load(open('sim.pkl','rb'))
def recommend(movie):
   index=movies[movies['Movie']==movie].index[0] 
   distances=sorted(list(enumerate(sim[index])),reverse=True,key = lambda x: x[1])[1:6]
   recommended_movies=[]
   for i in distances:
        movie_id =i[0]
        #fetch post from Api
        recommended_movies.append(movies.iloc[i[0]].Movie)
   return recommended_movies
        
        
movies_list =pickle.load(open('k1.pkl','rb'))
movies=pd.DataFrame(movies_list)


st.title('Tollywood Movie Recommender')
selected_movie_name = st.selectbox(
    'How would you like to find a movie?',
     movies['Movie'].values
)

if st.button('Recommend'):
    recomendations=recommend(selected_movie_name)
    for i in recomendations:
       st.write(i)