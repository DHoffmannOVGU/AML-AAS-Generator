from typing import Optional
import streamlit as st

from sqlmodel import Session, SQLModel, create_engine, select
from sqlalchemy.sql import text

from model import Hero


# hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
# hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
# hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


try:
    engine = create_engine("sqlite:///database.db")
    SQLModel.metadata.create_all(engine)
except:
    st.info("Database already exists")


def add_hero(hero: Hero):    
    with Session(engine) as session:
        session.add(hero)
        session.commit()
        session.refresh(hero)

def get_heroes():
    with Session(engine) as session:
        statement = session.exec(text("SELECT * FROM hero"))
        heroes = statement.fetchall()
        return heroes
    
def get_hero_by_name(name: str):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name=="David")
        statement = session.exec(statement)
        hero = statement.fetchall()
        return hero

def hero_adder_ui():
    name = st.text_input("Name", key="add_name")
    secret_name = st.text_input("Secret Name")
    age = st.number_input("Age", 0, 100, 0)
    if st.button("Add Hero"):
        hero = Hero(name=name, secret_name=secret_name, age=age)
        add_hero(hero)
        st.success("Hero Added")

def hero_getter_ui():
    def get_hero_list(name):
        if name != "":
            hero_list = get_hero_by_name(name) 
            return hero_list
        else:
            return []
    
    name = st.text_input("Name", key="get_name")
    if name == "":
        get_hero_btn = st.button("Get Hero", use_container_width=True, disabled=True)
    else:
        get_hero_btn = st.button("Get Hero", use_container_width=True, disabled=False)
    if get_hero_btn:
        return get_hero_list(name)
    else: 
        return []





st.title("SQLModel with SQLite")
hero_adder_ui()
hero_list = hero_getter_ui()
for hero in hero_list:
    st.write(hero)
    st.write(type(hero).__name__)
    st.write(hero.model_dump())


st.write(get_heroes())