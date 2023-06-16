import streamlit as st
import numpy as np
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt
import mpl_interactions.ipyplot as iplt
from matplotlib.markers import MarkerStyle

# pretty plots
color_list = [
    '#003f5c',
    '#d45087',
    '#2f4b7c',
    '#f95d6a',
    '#665191',
    '#ff7c43',
    '#a05195',
    '#ffa600',
]

plt.rcParams['font.sans-serif'] = 'Arial'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#909090'
plt.rcParams['axes.labelcolor'] = '#909090'
plt.rcParams['xtick.color'] = '#909090'
plt.rcParams['ytick.color'] = '#909090'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=color_list)
plt.rcParams['text.usetex'] = True

github_link = '[GitHub](https://github.com/amizarmo)'
linkedin_link = '[LinkedIn](https://www.linkedin.com/in/amir-zare-42b595201)'

tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ['Home', "1.1", "1.2", "1.3", '1.4', '1.5'])

with tab0:
    st.write('This is the corresponding web app to the BioMath101 course. Here you can play around with model parameters and observe how the behaviour changes.')
    st.markdown('---')
    st.write('by Amir Zare')
    st.markdown(linkedin_link, unsafe_allow_html=True)
    st.markdown(github_link, unsafe_allow_html=True)


with tab1:
    def plot_model_1(alpha, beta):
        def b(x): return x*alpha
        def d(x): return x*0 + beta

        plt.style.use('seaborn-white')
        x = np.arange(0, 11, 1)
        fig, ax = plt.subplots(figsize=(6, 4))

        ax.plot(x, b(x), lw=2, ls='-', label='removal', zorder=1)
        ax.plot(x, d(x), lw=2, ls='-', label='production', zorder=1)
        # ax.scatter(beta/alpha, beta,s = 100,color='white', alpha=1, edgecolor = 'black',linewidth = 2, zorder = 2)
        ax.scatter(beta/alpha, beta, s=100, color='black', alpha=1,
                   edgecolor='black', linewidth=2, zorder=2)
        # ax.scatter(2, beta,s = 100, marker=MarkerStyle("o", fillstyle="right"), color='black', alpha=1, edgecolor = 'black',linewidth = 2, zorder = 2)
        # ax.scatter(2, beta,s = 100, marker=MarkerStyle("o", fillstyle="left"), color='white', alpha=1, edgecolor = 'black',linewidth = 2, zorder = 2)

        plt.axvline(beta/alpha, ymin=0, ymax=1, ls='--',
                    color='gray', zorder=0, lw=1)
        plt.xlabel('$x$')
        plt.ylabel('$\dot{x}$', rotation='horizontal')

        plt.title('$fig \ 1.1$')
        plt.legend(frameon=True, ncol=1)
        plt.grid(True, alpha=0.5, lw=0.5)
        return fig

    st.write(r'''
    $\dot{x} = \beta- \alpha.x$
    ''')
    col1, col2 = st.columns([3, 1])
    with col2:
        alpha = st.slider('alpha', min_value=1, max_value=10)
        beta = st.slider('beta', min_value=1, max_value=10)

    with col1:
        st.pyplot(plot_model_1(alpha=alpha, beta=beta))

with tab2:
    st.write(r'''
    $\dot{x} = k_1.x - k_2.x^2$
    ''')

    def plot_model_2(k_1, k_2):
        def a(x): return k_1*x
        def b(x): return k_2*x**2

        plt.style.use('seaborn-white')
        x = np.arange(-1, 2, .1)
        fig, ax = plt.subplots(figsize=(6, 4))

        ax.plot(x, a(x), lw=2, ls='-', label='$k_1.a.x$')
        ax.plot(x, b(x), lw=2, ls='-', label='$k_2.x^2$')

        plt.xlabel('$x$')
        plt.ylabel('$\dot{x}$', rotation='horizontal')

        plt.title('$fig \ 1.2$')
        plt.legend(frameon=True, ncol=2)
        plt.grid(True, alpha=0.5, lw=0.5)
        return fig

    col1, col2 = st.columns([3, 1])
    with col2:
        k_1 = st.slider('k_1', min_value=1, max_value=10)
        k_2 = st.slider('k_2', min_value=1, max_value=10)

    with col1:
        st.pyplot(plot_model_2(k_1=k_1, k_2=k_2))

with tab3:
    st.markdown(r'$\dot{x} = \alpha x - \beta x y$')
    st.markdown(r'$\dot{y} = \delta x y - \gamma y$')

    def plot_model_3(alpha, beta, delta, gamma):
        def v_dot(v):
            x, y = v
            return [alpha*x - beta*x*y, delta*x*y - gamma*y]
        x = np.arange(0, 105, 5)
        y = np.arange(0, 63, 3)
        X, Y = np.meshgrid(x, y)
        x_dot, y_dot = v_dot([X, Y])

        plt.style.use('seaborn-white')
        fig1, ax = plt.subplots(figsize=(10, 8))

        m = np.hypot(x_dot, y_dot)
        m[m == 0] = 1
        x_dot /= m
        y_dot /= m

        ax.quiver(X, Y, x_dot, y_dot, m, pivot='mid', cmap='viridis')
        plt.grid(True, alpha=0.5, lw=0.5)

        fig2, ax = plt.subplots(figsize=(10, 8))
        ax.streamplot(X, Y, x_dot, y_dot, density=[
                      1, 1], color=m, cmap='autumn')
        plt.title('$fig \ 1.3$')
        plt.grid(True, alpha=0.5, lw=0.5)

        return fig1, fig2

    col1, col2 = st.columns([3, 1])
    with col2:
        alpha = st.slider('alpha', min_value=.01, max_value=1.)
        beta = st.slider('beta', min_value=.01, max_value=1.)
        delta = st.slider('delta', min_value=.01, max_value=1.)
        gamma = st.slider('gamma', min_value=.01, max_value=1.)

    with col1:
        st.pyplot(plot_model_3(alpha, beta, delta, gamma)[0])
        st.pyplot(plot_model_3(alpha, beta, delta, gamma)[1])

with tab4:

    st.markdown(r'$\dot x = r_xx(\frac{K_x-(x+\alpha y)}{K_x})$')
    st.markdown(r'$\dot y = r_yy(\frac{K_y-(y+\beta x)}{K_y})$')

    def plot_model_4(rx, ry, alpha, beta, kx, ky):
        def v_dot(v):
            x, y = v
            return [rx*x*(1-(x+alpha*y)/kx), ry*y*(1-(y+beta*x)/ky)]
        x = np.arange(0.0, 2.01, .01)
        y = np.arange(0.0, 2.01, .01)
        X, Y = np.meshgrid(x, y)
        x_dot, y_dot = v_dot([X, Y])

        plt.style.use('seaborn-white')
        fig1, ax = plt.subplots(figsize=(10, 8))

        ax.contour(X, Y, x_dot, levels=[0], colors='red', linewidths=3)
        ax.contour(X, Y, y_dot, levels=[0], colors='orange', linewidths=3)

        x = np.arange(0.0, 2.1, .1)
        y = np.arange(0.0, 2.1, .1)
        X, Y = np.meshgrid(x, y)
        x_dot, y_dot = v_dot([X, Y])
        m = np.hypot(x_dot, y_dot)
        m[m == 0] = 1
        x_dot_norm = x_dot/m
        y_dot_norm = y_dot/m

        ax.quiver(X, Y, x_dot_norm, y_dot_norm, m, pivot='mid', cmap='viridis')
        plt.title('$fig \ 1.4$')
        plt.grid(True, alpha=0.5, lw=0.5)

        fig2, ax = plt.subplots(figsize=(10, 8))
        ax.streamplot(X, Y, x_dot, y_dot, density=[
                      1.5, 1.5], color=m, cmap='autumn', linewidth=2)
        plt.title('$fig \ 1.4$')
        plt.grid(True, alpha=0.5, lw=0.5)

        return fig1, fig2

    col1, col2 = st.columns([3, 1])
    with col2:
        rx = st.slider('rx', min_value=.5, max_value=2.)
        ry = st.slider('ry', min_value=.5, max_value=2.)
        alpha = st.slider('alpha', min_value=0., max_value=1.)
        beta = st.slider('beta', min_value=0., max_value=1.)
        kx = st.slider('kx', min_value=1., max_value=2.)
        ky = st.slider('ky', min_value=1., max_value=2.)

    with col1:
        st.pyplot(plot_model_4(rx, ry, alpha, beta, kx, ky)[0])
        st.pyplot(plot_model_4(rx, ry, alpha, beta, kx, ky)[1])

with tab5:

    st.markdown(r'$\dot x = -ax-ry$')
    st.markdown(r'$\dot y = sx-dy$')

    def plot_model_5(a, r, s, d):
        def v_dot(v):
            x, y = v
            return [-a*x-r*y, s*x-d*y]
        x = np.arange(-2.0, 2.01, .2)
        y = np.arange(-2.0, 2.01, .2)
        X, Y = np.meshgrid(x, y)
        x_dot, y_dot = v_dot([X, Y])

        plt.style.use('seaborn-white')
        fig1, ax = plt.subplots(figsize=(10, 8))

        ax.contour(X, Y, x_dot, levels=[0], colors='red', linewidths=3)
        ax.contour(X, Y, y_dot, levels=[0], colors='orange', linewidths=3)

        x = np.arange(-2.0, 2.1, .2)
        y = np.arange(-2.0, 2.1, .2)
        X, Y = np.meshgrid(x, y)
        x_dot, y_dot = v_dot([X, Y])
        m = np.hypot(x_dot, y_dot)
        m[m == 0] = 1
        x_dot_norm = x_dot/m
        y_dot_norm = y_dot/m

        ax.quiver(X, Y, x_dot_norm, y_dot_norm, m, pivot='mid', cmap='viridis')
        plt.title('$fig \ 1.5$')
        plt.grid(True, alpha=0.5, lw=0.5)

        fig2, ax = plt.subplots(figsize=(10, 8))
        ax.streamplot(X, Y, x_dot, y_dot, density=[
                      1.5, 1.5], color=m, cmap='autumn', linewidth=2)
        plt.title('$fig \ 1.5$')
        plt.grid(True, alpha=0.5, lw=0.5)

        return fig1, fig2

    col1, col2 = st.columns([3, 1])
    with col2:
        a = st.slider('a', min_value=0.1, max_value=5.)
        r = st.slider('r', min_value=0.1, max_value=5.)
        s = st.slider('s', min_value=0.1, max_value=5.)
        d = st.slider('d', min_value=0.1, max_value=5.)

    with col1:
        st.pyplot(plot_model_5(a, r, s, d)[0])
        st.pyplot(plot_model_5(a, r, s, d)[1])
