PGDMP     8                    z         
   py_RestApi    12.6    12.6                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16716 
   py_RestApi    DATABASE     ?   CREATE DATABASE "py_RestApi" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Spanish_Colombia.1252' LC_CTYPE = 'Spanish_Colombia.1252';
    DROP DATABASE "py_RestApi";
                postgres    false            ?            1259    16725 
   employedbd    TABLE     ?   CREATE TABLE public.employedbd (
    id character(36) NOT NULL,
    name character varying(50),
    charge character varying(50),
    salary smallint,
    startdate date
);
    DROP TABLE public.employedbd;
       public         heap    postgres    false            ?            1259    16732    useraccount    TABLE     ?   CREATE TABLE public.useraccount (
    id integer NOT NULL,
    username character varying(100) NOT NULL,
    password character varying(150) NOT NULL
);
    DROP TABLE public.useraccount;
       public         heap    postgres    false            ?            1259    16730    useraccount_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.useraccount_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.useraccount_id_seq;
       public          postgres    false    204                       0    0    useraccount_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.useraccount_id_seq OWNED BY public.useraccount.id;
          public          postgres    false    203            ?
           2604    16735    useraccount id    DEFAULT     p   ALTER TABLE ONLY public.useraccount ALTER COLUMN id SET DEFAULT nextval('public.useraccount_id_seq'::regclass);
 =   ALTER TABLE public.useraccount ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    203    204    204                      0    16725 
   employedbd 
   TABLE DATA           I   COPY public.employedbd (id, name, charge, salary, startdate) FROM stdin;
    public          postgres    false    202   d                 0    16732    useraccount 
   TABLE DATA           =   COPY public.useraccount (id, username, password) FROM stdin;
    public          postgres    false    204   ?                  0    0    useraccount_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.useraccount_id_seq', 1, true);
          public          postgres    false    203            ?
           2606    16729    employedbd employedbd_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.employedbd
    ADD CONSTRAINT employedbd_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.employedbd DROP CONSTRAINT employedbd_pkey;
       public            postgres    false    202            ?
           2606    16737    useraccount useraccount_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.useraccount
    ADD CONSTRAINT useraccount_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.useraccount DROP CONSTRAINT useraccount_pkey;
       public            postgres    false    204                 x?u??j?0?s?y??}\?i0?uٖ??5)IZ??~NYwh蠋~?TRH??*"??D?b??F????<i?^x???1???????85(?h?{@???h,??b??1?-???@̬?fK?>woi^z?gh?⢡ ?uZ!??I#xU?b	<??b?\?[???L??h7?????_m??([??,??1?6??'U????.1?;?u?S?;??|???P??c?|???l?u??2???!?P_??Ʉ?d????/nc6?>???ڶ?}??L         v   x??1?0 ??yGgۉwE?}K?`?P?V??pCi???ǹ?s?i?ԥNǳ`?	?????
?2?u?~Ǫ)fH!I??????? $???????,?f??? ???9?X]#5     